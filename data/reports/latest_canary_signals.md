# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T10:37:27.716288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `13`; crypto_alt avg `-0.2092` n `239`; crypto_major avg `-0.0786` n `8`; equity avg `-0.0046` n `158`; fx avg `0.0064` n `6`; index avg `-0.0009` n `27`; metal avg `0.0377` n `20`; unknown avg `0.2301` n `1253`
- 1h: commodity avg `0.1445` n `13`; crypto_alt avg `-0.3724` n `239`; crypto_major avg `-0.1009` n `8`; equity avg `0.0206` n `158`; fx avg `0.0114` n `6`; index avg `0.0139` n `27`; metal avg `0.0206` n `20`; unknown avg `0.209` n `1235`
- 4h: commodity avg `0.4698` n `13`; crypto_alt avg `-0.1163` n `239`; crypto_major avg `0.1837` n `8`; equity avg `0.5143` n `158`; fx avg `-0.0339` n `6`; index avg `0.0922` n `27`; metal avg `0.0587` n `20`; unknown avg `0.7142` n `1145`
- 24h: commodity avg `-1.2254` n `13`; crypto_alt avg `0.3978` n `239`; crypto_major avg `1.406` n `8`; equity avg `-3.4227` n `158`; fx avg `-0.0191` n `6`; index avg `-0.2852` n `27`; metal avg `0.5525` n `20`; unknown avg `0.7017` n `1074`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2483`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
