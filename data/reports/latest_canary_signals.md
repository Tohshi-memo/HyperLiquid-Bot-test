# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T17:22:50.099762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0597` n `12`; crypto_alt avg `-0.0461` n `230`; crypto_major avg `-0.0886` n `8`; equity avg `-0.0034` n `108`; fx avg `0.0055` n `6`; index avg `-0.0215` n `25`; metal avg `-0.0212` n `20`; unknown avg `0.0346` n `782`
- 1h: commodity avg `-0.2167` n `12`; crypto_alt avg `-0.0214` n `230`; crypto_major avg `-0.1799` n `8`; equity avg `-0.2563` n `108`; fx avg `-0.0096` n `6`; index avg `-0.0357` n `25`; metal avg `0.041` n `20`; unknown avg `-0.02` n `782`
- 4h: commodity avg `-0.289` n `12`; crypto_alt avg `0.1439` n `230`; crypto_major avg `0.4101` n `8`; equity avg `0.0034` n `108`; fx avg `-0.0215` n `6`; index avg `-0.1` n `25`; metal avg `0.1886` n `20`; unknown avg `0.0025` n `782`
- 24h: commodity avg `-0.1812` n `12`; crypto_alt avg `0.6906` n `230`; crypto_major avg `0.6349` n `8`; equity avg `-0.1211` n `108`; fx avg `0.0089` n `6`; index avg `0.002` n `25`; metal avg `0.567` n `20`; unknown avg `0.7201` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
