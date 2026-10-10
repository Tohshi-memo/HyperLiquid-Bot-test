# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T16:22:28.138525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0807` n `13`; crypto_alt avg `0.0927` n `235`; crypto_major avg `-0.015` n `8`; equity avg `0.0048` n `150`; fx avg `-0.0006` n `6`; index avg `0.0027` n `26`; metal avg `-0.0043` n `20`; unknown avg `38.5201` n `1117`
- 1h: commodity avg `-0.0798` n `13`; crypto_alt avg `0.1876` n `235`; crypto_major avg `-0.1055` n `8`; equity avg `0.0092` n `150`; fx avg `-0.0017` n `6`; index avg `0.0014` n `26`; metal avg `-0.018` n `20`; unknown avg `4.6135` n `1109`
- 4h: commodity avg `0.0123` n `13`; crypto_alt avg `0.9663` n `235`; crypto_major avg `0.5024` n `8`; equity avg `0.1102` n `150`; fx avg `-0.0068` n `6`; index avg `0.0179` n `26`; metal avg `-0.0174` n `20`; unknown avg `1.61` n `1101`
- 24h: commodity avg `-0.5202` n `13`; crypto_alt avg `2.3988` n `235`; crypto_major avg `0.8632` n `8`; equity avg `0.434` n `150`; fx avg `0.0211` n `6`; index avg `0.0597` n `26`; metal avg `0.0111` n `20`; unknown avg `2.2308` n `984`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
