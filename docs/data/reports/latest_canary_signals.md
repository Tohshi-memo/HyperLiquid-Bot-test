# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T20:22:27.228908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.1529` n `228`; crypto_major avg `-0.31` n `8`; equity avg `-0.0278` n `88`; fx avg `-0.0029` n `6`; index avg `-0.0324` n `23`; metal avg `-0.0571` n `20`; unknown avg `-0.0845` n `765`
- 1h: commodity avg `0.0042` n `12`; crypto_alt avg `-0.0106` n `228`; crypto_major avg `0.0986` n `8`; equity avg `0.1048` n `88`; fx avg `0.0263` n `6`; index avg `-0.0505` n `23`; metal avg `-0.1151` n `20`; unknown avg `1.75` n `763`
- 4h: commodity avg `-0.1761` n `12`; crypto_alt avg `0.1145` n `228`; crypto_major avg `0.6612` n `8`; equity avg `0.4852` n `88`; fx avg `0.0034` n `6`; index avg `-0.0165` n `23`; metal avg `-0.1682` n `20`; unknown avg `1.4272` n `763`
- 24h: commodity avg `0.1261` n `12`; crypto_alt avg `-2.393` n `228`; crypto_major avg `-2.3055` n `8`; equity avg `1.2096` n `88`; fx avg `0.1495` n `6`; index avg `0.2386` n `23`; metal avg `0.0717` n `20`; unknown avg `8.0985` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
