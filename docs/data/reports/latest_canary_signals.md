# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T10:52:30.858326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0244` n `12`; crypto_alt avg `-0.1086` n `230`; crypto_major avg `0.0122` n `8`; equity avg `-0.0435` n `112`; fx avg `0.0029` n `6`; index avg `0.0005` n `25`; metal avg `-0.0312` n `20`; unknown avg `-0.014` n `782`
- 1h: commodity avg `-0.1265` n `12`; crypto_alt avg `-0.0959` n `230`; crypto_major avg `0.0034` n `8`; equity avg `-0.1504` n `112`; fx avg `-0.0053` n `6`; index avg `-0.009` n `25`; metal avg `-0.129` n `20`; unknown avg `-0.0772` n `782`
- 4h: commodity avg `-0.3611` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `0.7852` n `8`; equity avg `0.5433` n `112`; fx avg `-0.0176` n `6`; index avg `0.0823` n `25`; metal avg `0.1009` n `20`; unknown avg `0.1421` n `782`
- 24h: commodity avg `0.1088` n `12`; crypto_alt avg `0.6014` n `230`; crypto_major avg `0.3099` n `8`; equity avg `2.0664` n `109`; fx avg `-0.0886` n `6`; index avg `0.0724` n `25`; metal avg `0.2531` n `20`; unknown avg `0.3615` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
