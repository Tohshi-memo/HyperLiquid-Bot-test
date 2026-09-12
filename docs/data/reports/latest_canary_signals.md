# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T20:07:27.422268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `0.1256` n `233`; crypto_major avg `0.1514` n `8`; equity avg `-0.0355` n `136`; fx avg `0.0012` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0106` n `20`; unknown avg `-0.0167` n `836`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `-0.1477` n `233`; crypto_major avg `-0.0818` n `8`; equity avg `-0.2182` n `136`; fx avg `-0.0075` n `6`; index avg `-0.0198` n `26`; metal avg `-0.008` n `20`; unknown avg `0.74` n `836`
- 4h: commodity avg `0.0816` n `12`; crypto_alt avg `-0.4574` n `233`; crypto_major avg `-0.4102` n `8`; equity avg `-0.2473` n `136`; fx avg `0.0` n `6`; index avg `-0.0292` n `26`; metal avg `-0.0051` n `20`; unknown avg `0.2766` n `782`
- 24h: commodity avg `-0.1603` n `12`; crypto_alt avg `0.6119` n `233`; crypto_major avg `-0.5044` n `8`; equity avg `-0.2399` n `136`; fx avg `-0.0333` n `6`; index avg `0.0139` n `26`; metal avg `-0.0061` n `20`; unknown avg `5.8129` n `722`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
