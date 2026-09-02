# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T18:48:20.929594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `0.027` n `232`; crypto_major avg `0.0637` n `8`; equity avg `0.0449` n `133`; fx avg `0.0071` n `6`; index avg `-0.0034` n `26`; metal avg `-0.007` n `20`; unknown avg `-0.1397` n `792`
- 1h: commodity avg `0.0243` n `12`; crypto_alt avg `0.0597` n `232`; crypto_major avg `0.0415` n `8`; equity avg `0.3942` n `133`; fx avg `0.0091` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.3586` n `790`
- 4h: commodity avg `0.0371` n `12`; crypto_alt avg `0.2114` n `232`; crypto_major avg `0.1181` n `8`; equity avg `0.7121` n `133`; fx avg `-0.0047` n `6`; index avg `0.0418` n `26`; metal avg `-0.0093` n `20`; unknown avg `-0.6162` n `789`
- 24h: commodity avg `0.1739` n `12`; crypto_alt avg `0.1353` n `232`; crypto_major avg `0.0187` n `8`; equity avg `0.9339` n `133`; fx avg `-0.3553` n `6`; index avg `0.173` n `26`; metal avg `0.4063` n `20`; unknown avg `-0.168` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.043`, n `668`, weak_sample_signal
