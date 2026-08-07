# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T21:07:39.592138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `0.1041` n `230`; crypto_major avg `-0.0093` n `8`; equity avg `-0.0115` n `112`; fx avg `0.0154` n `6`; index avg `0.0015` n `25`; metal avg `0.0507` n `20`; unknown avg `0.0146` n `782`
- 1h: commodity avg `0.0457` n `12`; crypto_alt avg `-0.0736` n `230`; crypto_major avg `-0.0997` n `8`; equity avg `0.04` n `112`; fx avg `0.0165` n `6`; index avg `0.0152` n `25`; metal avg `0.0525` n `20`; unknown avg `0.2173` n `782`
- 4h: commodity avg `-0.1961` n `12`; crypto_alt avg `0.0346` n `230`; crypto_major avg `0.3108` n `8`; equity avg `0.4296` n `112`; fx avg `0.0144` n `6`; index avg `0.0584` n `25`; metal avg `0.0999` n `20`; unknown avg `-0.1812` n `782`
- 24h: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.0889` n `230`; crypto_major avg `-0.0246` n `8`; equity avg `2.1203` n `112`; fx avg `-0.1353` n `6`; index avg `0.1217` n `25`; metal avg `0.4018` n `20`; unknown avg `0.0194` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
