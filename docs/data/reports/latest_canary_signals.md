# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T20:52:27.574255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5777` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9028` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7179` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0306` n `13`; crypto_alt avg `0.0116` n `239`; crypto_major avg `-0.0006` n `8`; equity avg `0.1847` n `166`; fx avg `-0.0077` n `6`; index avg `0.0183` n `27`; metal avg `0.1156` n `20`; unknown avg `159.6034` n `1262`
- 1h: commodity avg `0.2029` n `13`; crypto_alt avg `-0.3649` n `239`; crypto_major avg `-0.3038` n `8`; equity avg `-0.3793` n `166`; fx avg `-0.0092` n `6`; index avg `-0.093` n `27`; metal avg `0.0333` n `20`; unknown avg `12.6009` n `1248`
- 4h: commodity avg `0.5611` n `13`; crypto_alt avg `-0.9944` n `239`; crypto_major avg `-2.0166` n `8`; equity avg `-1.5815` n `166`; fx avg `-0.0348` n `6`; index avg `-0.2987` n `27`; metal avg `-0.1138` n `20`; unknown avg `12.4827` n `1249`
- 24h: commodity avg `0.3222` n `13`; crypto_alt avg `-6.4138` n `239`; crypto_major avg `-7.3815` n `8`; equity avg `-8.6634` n `166`; fx avg `-0.0145` n `6`; index avg `-0.9059` n `27`; metal avg `-1.2024` n `20`; unknown avg `54.2572` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
