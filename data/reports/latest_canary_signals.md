# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T05:07:31.959637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `0.1802` n `230`; crypto_major avg `0.0051` n `8`; equity avg `0.273` n `112`; fx avg `-0.0028` n `6`; index avg `0.0508` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.0198` n `782`
- 1h: commodity avg `0.0522` n `12`; crypto_alt avg `-0.0352` n `230`; crypto_major avg `-0.2582` n `8`; equity avg `0.1086` n `112`; fx avg `-0.0104` n `6`; index avg `0.0485` n `25`; metal avg `-0.0579` n `20`; unknown avg `-0.294` n `782`
- 4h: commodity avg `0.1411` n `12`; crypto_alt avg `-0.448` n `230`; crypto_major avg `-0.6113` n `8`; equity avg `0.2472` n `112`; fx avg `-0.0324` n `6`; index avg `-0.0573` n `25`; metal avg `0.0987` n `20`; unknown avg `-0.4842` n `782`
- 24h: commodity avg `0.7377` n `12`; crypto_alt avg `-0.0963` n `230`; crypto_major avg `-1.5173` n `8`; equity avg `0.6137` n `109`; fx avg `0.014` n `6`; index avg `-0.1516` n `25`; metal avg `-0.0353` n `20`; unknown avg `113.1669` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
