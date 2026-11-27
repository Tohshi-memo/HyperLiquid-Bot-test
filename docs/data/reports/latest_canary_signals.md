# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T05:07:27.046561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0365` n `13`; crypto_alt avg `0.1657` n `239`; crypto_major avg `0.3285` n `8`; equity avg `0.4339` n `168`; fx avg `0.0182` n `6`; index avg `0.0242` n `27`; metal avg `0.0536` n `20`; unknown avg `8.5456` n `1249`
- 1h: commodity avg `0.0347` n `13`; crypto_alt avg `0.3124` n `239`; crypto_major avg `0.5028` n `8`; equity avg `0.6592` n `168`; fx avg `-0.0063` n `6`; index avg `0.0436` n `27`; metal avg `0.0833` n `20`; unknown avg `167.5703` n `1257`
- 4h: commodity avg `0.1906` n `13`; crypto_alt avg `1.3355` n `239`; crypto_major avg `2.1293` n `8`; equity avg `3.0713` n `168`; fx avg `0.0099` n `6`; index avg `0.2865` n `27`; metal avg `0.8858` n `20`; unknown avg `183.9466` n `1251`
- 24h: commodity avg `0.2715` n `13`; crypto_alt avg `1.9893` n `239`; crypto_major avg `2.1455` n `8`; equity avg `2.7708` n `168`; fx avg `0.028` n `6`; index avg `0.2435` n `27`; metal avg `0.6982` n `20`; unknown avg `206.7339` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
