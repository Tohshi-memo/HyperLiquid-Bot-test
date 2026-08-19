# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T04:52:25.681900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `-0.0381` n `230`; crypto_major avg `-0.057` n `8`; equity avg `-0.2284` n `120`; fx avg `-0.0114` n `6`; index avg `-0.057` n `25`; metal avg `-0.0418` n `20`; unknown avg `-0.0258` n `789`
- 1h: commodity avg `0.0123` n `12`; crypto_alt avg `-0.2608` n `230`; crypto_major avg `-0.0559` n `8`; equity avg `-0.437` n `120`; fx avg `-0.013` n `6`; index avg `-0.0937` n `25`; metal avg `-0.1107` n `20`; unknown avg `0.5958` n `789`
- 4h: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.0678` n `230`; crypto_major avg `-0.1456` n `8`; equity avg `-0.2623` n `120`; fx avg `-0.1059` n `6`; index avg `-0.098` n `25`; metal avg `-0.0537` n `20`; unknown avg `-0.0719` n `789`
- 24h: commodity avg `0.3043` n `12`; crypto_alt avg `0.4318` n `230`; crypto_major avg `0.1947` n `8`; equity avg `-3.5791` n `120`; fx avg `-0.1838` n `6`; index avg `-0.5938` n `25`; metal avg `-0.6267` n `20`; unknown avg `-0.2794` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
