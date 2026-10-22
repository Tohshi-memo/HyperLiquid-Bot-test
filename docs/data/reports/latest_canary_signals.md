# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T17:07:35.697091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7443` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0371` n `13`; crypto_alt avg `0.4425` n `237`; crypto_major avg `0.3241` n `8`; equity avg `-0.0252` n `151`; fx avg `0.0037` n `6`; index avg `0.0112` n `26`; metal avg `0.0177` n `20`; unknown avg `0.541` n `1231`
- 1h: commodity avg `0.1019` n `13`; crypto_alt avg `-0.5918` n `237`; crypto_major avg `-0.8742` n `8`; equity avg `-0.9052` n `151`; fx avg `0.0032` n `6`; index avg `-0.1146` n `26`; metal avg `-0.0896` n `20`; unknown avg `5.3179` n `1231`
- 4h: commodity avg `-0.1043` n `13`; crypto_alt avg `-1.2712` n `237`; crypto_major avg `-0.8134` n `8`; equity avg `-2.5577` n `151`; fx avg `0.0381` n `6`; index avg `-0.2154` n `26`; metal avg `-0.3038` n `20`; unknown avg `2.2955` n `1083`
- 24h: commodity avg `0.4733` n `13`; crypto_alt avg `-5.2711` n `237`; crypto_major avg `-4.1377` n `8`; equity avg `-5.2481` n `151`; fx avg `-0.1382` n `6`; index avg `-0.6614` n `26`; metal avg `-0.9908` n `20`; unknown avg `6.3639` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
