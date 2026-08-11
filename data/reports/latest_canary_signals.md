# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T08:22:32.047949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0531` n `12`; crypto_alt avg `0.0199` n `230`; crypto_major avg `-0.0651` n `8`; equity avg `-0.1852` n `113`; fx avg `0.006` n `6`; index avg `-0.0289` n `25`; metal avg `-0.0208` n `20`; unknown avg `-0.0074` n `785`
- 1h: commodity avg `0.0547` n `12`; crypto_alt avg `0.0717` n `230`; crypto_major avg `0.1986` n `8`; equity avg `-0.0599` n `113`; fx avg `-0.002` n `6`; index avg `-0.0024` n `25`; metal avg `0.0726` n `20`; unknown avg `0.0142` n `785`
- 4h: commodity avg `0.4468` n `12`; crypto_alt avg `-0.5383` n `230`; crypto_major avg `-0.3144` n `8`; equity avg `-0.5076` n `113`; fx avg `0.0376` n `6`; index avg `-0.0919` n `25`; metal avg `-0.2631` n `20`; unknown avg `-0.0535` n `753`
- 24h: commodity avg `1.22` n `12`; crypto_alt avg `-1.3814` n `230`; crypto_major avg `-1.1879` n `8`; equity avg `-1.5894` n `113`; fx avg `0.0325` n `6`; index avg `-0.0799` n `25`; metal avg `0.1197` n `20`; unknown avg `0.0804` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
