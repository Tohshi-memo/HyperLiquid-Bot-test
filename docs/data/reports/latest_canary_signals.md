# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T12:52:25.566357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.0708` n `231`; crypto_major avg `0.1189` n `8`; equity avg `-0.1052` n `122`; fx avg `0.0103` n `6`; index avg `-0.0144` n `25`; metal avg `-0.0105` n `20`; unknown avg `0.2065` n `797`
- 1h: commodity avg `-0.0898` n `12`; crypto_alt avg `-0.0798` n `231`; crypto_major avg `-0.0846` n `8`; equity avg `-0.4052` n `122`; fx avg `-0.0122` n `6`; index avg `-0.047` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.0744` n `797`
- 4h: commodity avg `0.1583` n `12`; crypto_alt avg `-0.3425` n `231`; crypto_major avg `-0.2539` n `8`; equity avg `-0.4923` n `122`; fx avg `-0.0089` n `6`; index avg `-0.0532` n `25`; metal avg `-0.0387` n `20`; unknown avg `-0.0393` n `797`
- 24h: commodity avg `-0.067` n `12`; crypto_alt avg `-1.3712` n `231`; crypto_major avg `-1.1724` n `8`; equity avg `-0.1602` n `122`; fx avg `-0.0275` n `6`; index avg `-0.0639` n `25`; metal avg `0.0971` n `20`; unknown avg `0.68` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
