# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T07:52:28.916616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0225` n `12`; crypto_alt avg `0.0493` n `230`; crypto_major avg `0.0006` n `8`; equity avg `0.0225` n `113`; fx avg `-0.0076` n `6`; index avg `-0.0037` n `25`; metal avg `0.0559` n `20`; unknown avg `-0.0157` n `786`
- 1h: commodity avg `0.1423` n `12`; crypto_alt avg `-0.1422` n `230`; crypto_major avg `0.1179` n `8`; equity avg `0.1914` n `113`; fx avg `0.0071` n `6`; index avg `-0.0057` n `25`; metal avg `0.026` n `20`; unknown avg `0.0026` n `786`
- 4h: commodity avg `-0.0321` n `12`; crypto_alt avg `-0.5363` n `230`; crypto_major avg `-0.0946` n `8`; equity avg `0.1188` n `113`; fx avg `0.0116` n `6`; index avg `-0.0014` n `25`; metal avg `0.1232` n `20`; unknown avg `-0.0577` n `770`
- 24h: commodity avg `-0.0566` n `12`; crypto_alt avg `-0.9677` n `230`; crypto_major avg `0.7454` n `8`; equity avg `2.1006` n `113`; fx avg `0.0211` n `6`; index avg `0.1866` n `25`; metal avg `0.3616` n `20`; unknown avg `-0.1297` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2268`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
