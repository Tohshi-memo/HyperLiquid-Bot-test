# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T13:22:21.750265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.29` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.104` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.3344` n `12`; crypto_alt avg `-0.002` n `228`; crypto_major avg `0.1672` n `8`; equity avg `-0.1046` n `66`; fx avg `-0.0163` n `6`; index avg `0.0138` n `23`; metal avg `-0.1351` n `18`; unknown avg `-0.0272` n `386`
- 1h: commodity avg `0.4243` n `12`; crypto_alt avg `0.52` n `228`; crypto_major avg `0.5689` n `8`; equity avg `0.0332` n `66`; fx avg `-0.0062` n `6`; index avg `0.0418` n `23`; metal avg `0.1245` n `18`; unknown avg `-0.1377` n `386`
- 4h: commodity avg `1.4165` n `12`; crypto_alt avg `-0.7074` n `228`; crypto_major avg `-0.6875` n `8`; equity avg `-0.5899` n `66`; fx avg `-0.0201` n `6`; index avg `-0.3928` n `23`; metal avg `-0.7649` n `18`; unknown avg `1.3929` n `386`
- 24h: commodity avg `-0.2897` n `12`; crypto_alt avg `1.9024` n `228`; crypto_major avg `2.2753` n `8`; equity avg `0.9613` n `66`; fx avg `0.0305` n `6`; index avg `0.8671` n `23`; metal avg `-0.1022` n `18`; unknown avg `6.0174` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
