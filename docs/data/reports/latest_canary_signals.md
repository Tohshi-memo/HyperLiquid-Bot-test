# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T15:37:26.972018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0409` n `12`; crypto_alt avg `0.0939` n `231`; crypto_major avg `0.1698` n `8`; equity avg `0.1356` n `122`; fx avg `-0.0161` n `6`; index avg `0.0356` n `25`; metal avg `0.0766` n `20`; unknown avg `0.0545` n `795`
- 1h: commodity avg `-0.1098` n `12`; crypto_alt avg `-0.2884` n `231`; crypto_major avg `-0.0059` n `8`; equity avg `0.1714` n `122`; fx avg `-0.0125` n `6`; index avg `0.0455` n `25`; metal avg `0.1309` n `20`; unknown avg `0.0337` n `795`
- 4h: commodity avg `-0.1298` n `12`; crypto_alt avg `-0.8024` n `231`; crypto_major avg `-0.4241` n `8`; equity avg `0.3808` n `122`; fx avg `0.007` n `6`; index avg `-0.0353` n `25`; metal avg `0.1378` n `20`; unknown avg `-0.1288` n `795`
- 24h: commodity avg `-0.6406` n `12`; crypto_alt avg `-1.9141` n `231`; crypto_major avg `-0.7974` n `8`; equity avg `1.5969` n `122`; fx avg `0.0175` n `6`; index avg `0.2164` n `25`; metal avg `-0.2775` n `20`; unknown avg `-1.0633` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
