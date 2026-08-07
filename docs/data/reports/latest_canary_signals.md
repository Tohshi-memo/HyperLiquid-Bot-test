# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T13:37:30.623518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0376` n `12`; crypto_alt avg `0.0181` n `230`; crypto_major avg `-0.0908` n `8`; equity avg `-0.5291` n `112`; fx avg `0.0116` n `6`; index avg `-0.0251` n `25`; metal avg `0.0695` n `20`; unknown avg `0.0611` n `782`
- 1h: commodity avg `0.1045` n `12`; crypto_alt avg `0.053` n `230`; crypto_major avg `0.0916` n `8`; equity avg `-0.3079` n `112`; fx avg `0.0535` n `6`; index avg `-0.0332` n `25`; metal avg `-0.0431` n `20`; unknown avg `-0.0136` n `782`
- 4h: commodity avg `0.031` n `12`; crypto_alt avg `0.0162` n `230`; crypto_major avg `0.2986` n `8`; equity avg `0.2852` n `112`; fx avg `-0.0453` n `6`; index avg `0.0977` n `25`; metal avg `-0.0468` n `20`; unknown avg `0.0232` n `782`
- 24h: commodity avg `0.2768` n `12`; crypto_alt avg `0.5095` n `230`; crypto_major avg `1.0051` n `8`; equity avg `2.7244` n `109`; fx avg `-0.1295` n `6`; index avg `0.2077` n `25`; metal avg `0.4573` n `20`; unknown avg `0.3084` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
