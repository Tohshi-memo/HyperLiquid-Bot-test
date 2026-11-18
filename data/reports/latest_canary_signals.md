# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T01:52:31.605516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `13`; crypto_alt avg `-0.0656` n `239`; crypto_major avg `-0.0398` n `8`; equity avg `-0.2803` n `163`; fx avg `0.0012` n `6`; index avg `-0.0362` n `27`; metal avg `-0.1057` n `20`; unknown avg `1.0077` n `1266`
- 1h: commodity avg `-0.1159` n `13`; crypto_alt avg `-0.4866` n `239`; crypto_major avg `-0.6193` n `8`; equity avg `-1.5406` n `163`; fx avg `-0.0048` n `6`; index avg `-0.2032` n `27`; metal avg `-0.0505` n `20`; unknown avg `2.218` n `1264`
- 4h: commodity avg `-0.1245` n `13`; crypto_alt avg `0.186` n `239`; crypto_major avg `0.3291` n `8`; equity avg `0.4699` n `163`; fx avg `-0.0643` n `6`; index avg `-0.0298` n `27`; metal avg `-0.2587` n `20`; unknown avg `168.2059` n `1211`
- 24h: commodity avg `0.236` n `13`; crypto_alt avg `0.5205` n `239`; crypto_major avg `0.4268` n `8`; equity avg `-0.0977` n `163`; fx avg `-0.0913` n `6`; index avg `-0.1189` n `27`; metal avg `-0.4538` n `20`; unknown avg `6.9491` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
