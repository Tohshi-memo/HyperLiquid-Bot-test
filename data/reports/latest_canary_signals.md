# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T10:37:34.104757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0441` n `13`; crypto_alt avg `-0.1782` n `239`; crypto_major avg `-0.445` n `8`; equity avg `0.0228` n `163`; fx avg `0.0127` n `6`; index avg `0.0083` n `27`; metal avg `0.0159` n `20`; unknown avg `0.5323` n `1266`
- 1h: commodity avg `0.0037` n `13`; crypto_alt avg `-0.2965` n `239`; crypto_major avg `-0.6159` n `8`; equity avg `-0.2174` n `163`; fx avg `0.0191` n `6`; index avg `-0.0187` n `27`; metal avg `-0.0458` n `20`; unknown avg `4.6317` n `1262`
- 4h: commodity avg `0.0632` n `13`; crypto_alt avg `0.0226` n `239`; crypto_major avg `-0.3589` n `8`; equity avg `0.4489` n `163`; fx avg `-0.0496` n `6`; index avg `0.0833` n `27`; metal avg `-0.2278` n `20`; unknown avg `104.2375` n `1186`
- 24h: commodity avg `-0.1385` n `13`; crypto_alt avg `0.9811` n `239`; crypto_major avg `0.9815` n `8`; equity avg `1.8525` n `163`; fx avg `-0.0829` n `6`; index avg `0.1552` n `27`; metal avg `-0.9752` n `20`; unknown avg `5.8775` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
