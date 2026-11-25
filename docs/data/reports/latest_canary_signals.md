# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T05:37:31.164560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0294` n `13`; crypto_alt avg `-0.103` n `239`; crypto_major avg `-0.0863` n `8`; equity avg `-0.1472` n `168`; fx avg `0.0099` n `6`; index avg `-0.0154` n `27`; metal avg `-0.1096` n `20`; unknown avg `157.8505` n `1265`
- 1h: commodity avg `-0.0964` n `13`; crypto_alt avg `0.1728` n `239`; crypto_major avg `-0.1898` n `8`; equity avg `-0.4756` n `168`; fx avg `-0.0036` n `6`; index avg `-0.0424` n `27`; metal avg `-0.1492` n `20`; unknown avg `-0.3188` n `1259`
- 4h: commodity avg `-0.2861` n `13`; crypto_alt avg `0.4517` n `239`; crypto_major avg `-0.5997` n `8`; equity avg `-1.6011` n `168`; fx avg `-0.0424` n `6`; index avg `-0.1253` n `27`; metal avg `-0.3228` n `20`; unknown avg `1.7304` n `1245`
- 24h: commodity avg `0.4706` n `13`; crypto_alt avg `-3.6379` n `239`; crypto_major avg `-3.8067` n `8`; equity avg `-5.7416` n `167`; fx avg `0.123` n `6`; index avg `-0.5692` n `27`; metal avg `-1.1148` n `20`; unknown avg `694.6308` n `1029`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
