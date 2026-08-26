# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T05:52:23.479506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `0.0841` n `231`; crypto_major avg `-0.0269` n `8`; equity avg `-0.0343` n `122`; fx avg `-0.0098` n `6`; index avg `-0.0057` n `25`; metal avg `0.0099` n `20`; unknown avg `-0.0597` n `797`
- 1h: commodity avg `0.073` n `12`; crypto_alt avg `0.2581` n `231`; crypto_major avg `0.2938` n `8`; equity avg `-0.1705` n `122`; fx avg `-0.0113` n `6`; index avg `-0.0236` n `25`; metal avg `0.0249` n `20`; unknown avg `7.0656` n `797`
- 4h: commodity avg `0.0618` n `12`; crypto_alt avg `0.4085` n `231`; crypto_major avg `0.3966` n `8`; equity avg `0.5537` n `122`; fx avg `0.0015` n `6`; index avg `0.1321` n `25`; metal avg `-0.0185` n `20`; unknown avg `8.171` n `796`
- 24h: commodity avg `-0.5626` n `12`; crypto_alt avg `-2.8922` n `231`; crypto_major avg `-2.7537` n `8`; equity avg `0.8003` n `122`; fx avg `-0.0122` n `6`; index avg `0.117` n `25`; metal avg `0.2715` n `20`; unknown avg `0.5574` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
