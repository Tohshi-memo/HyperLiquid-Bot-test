# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T10:22:27.179356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0187` n `10`; crypto_alt avg `-0.0322` n `232`; crypto_major avg `-0.0181` n `7`; equity avg `0.0371` n `132`; fx avg `-0.0067` n `6`; index avg `0.0007` n `23`; metal avg `0.0743` n `13`; unknown avg `0.0198` n `900`
- 1h: commodity avg `-0.1171` n `12`; crypto_alt avg `0.1269` n `234`; crypto_major avg `0.0988` n `8`; equity avg `0.0193` n `137`; fx avg `-0.0243` n `6`; index avg `0.0192` n `27`; metal avg `0.0875` n `20`; unknown avg `0.3919` n `917`
- 4h: commodity avg `-0.0461` n `12`; crypto_alt avg `-0.1801` n `234`; crypto_major avg `-0.0405` n `8`; equity avg `0.117` n `137`; fx avg `-0.0304` n `6`; index avg `0.001` n `27`; metal avg `0.0302` n `20`; unknown avg `-0.247` n `911`
- 24h: commodity avg `0.082` n `12`; crypto_alt avg `-2.8528` n `234`; crypto_major avg `-2.7292` n `8`; equity avg `-0.1372` n `137`; fx avg `0.1068` n `6`; index avg `0.0976` n `27`; metal avg `0.5321` n `20`; unknown avg `18889.1909` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
