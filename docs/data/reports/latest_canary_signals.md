# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T09:22:31.977638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.77` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `0.0865` n `230`; crypto_major avg `0.0721` n `8`; equity avg `0.0876` n `102`; fx avg `0.0054` n `6`; index avg `0.0033` n `25`; metal avg `0.0078` n `20`; unknown avg `0.0505` n `777`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `0.1745` n `230`; crypto_major avg `0.1641` n `8`; equity avg `0.8587` n `102`; fx avg `0.0234` n `6`; index avg `0.0753` n `25`; metal avg `-0.0189` n `20`; unknown avg `-0.0841` n `777`
- 4h: commodity avg `-0.0299` n `12`; crypto_alt avg `0.3624` n `230`; crypto_major avg `0.499` n `8`; equity avg `1.447` n `102`; fx avg `0.0992` n `6`; index avg `0.3767` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.1777` n `761`
- 24h: commodity avg `0.0282` n `12`; crypto_alt avg `-1.1003` n `230`; crypto_major avg `1.0706` n `8`; equity avg `-0.8965` n `102`; fx avg `-0.083` n `6`; index avg `-0.1212` n `25`; metal avg `-0.0573` n `20`; unknown avg `-0.5658` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
