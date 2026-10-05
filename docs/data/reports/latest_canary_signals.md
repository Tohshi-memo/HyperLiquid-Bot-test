# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T04:22:33.026725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0301` n `13`; crypto_alt avg `-0.0166` n `235`; crypto_major avg `-0.1806` n `8`; equity avg `-0.0136` n `144`; fx avg `0.0154` n `6`; index avg `0.0049` n `26`; metal avg `-0.0557` n `20`; unknown avg `0.7102` n `1069`
- 1h: commodity avg `-0.0619` n `13`; crypto_alt avg `-0.2981` n `235`; crypto_major avg `-0.4074` n `8`; equity avg `-0.115` n `144`; fx avg `-0.0016` n `6`; index avg `-0.0251` n `26`; metal avg `-0.0488` n `20`; unknown avg `1.1966` n `998`
- 4h: commodity avg `-0.1327` n `13`; crypto_alt avg `-0.4222` n `235`; crypto_major avg `-0.5508` n `8`; equity avg `-0.2096` n `144`; fx avg `-0.1164` n `6`; index avg `-0.0707` n `26`; metal avg `-0.1132` n `20`; unknown avg `1.3548` n `978`
- 24h: commodity avg `-0.3592` n `13`; crypto_alt avg `0.3828` n `235`; crypto_major avg `0.8648` n `8`; equity avg `0.2874` n `144`; fx avg `-0.1028` n `6`; index avg `-0.0327` n `26`; metal avg `0.0265` n `20`; unknown avg `0.2584` n `906`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
