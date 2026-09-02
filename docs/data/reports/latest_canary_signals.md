# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T10:37:29.843422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3072` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0504` n `12`; crypto_alt avg `-0.166` n `232`; crypto_major avg `-0.1556` n `8`; equity avg `-0.0572` n `132`; fx avg `-0.0125` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0387` n `20`; unknown avg `-0.0978` n `792`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `-0.4643` n `232`; crypto_major avg `-0.1544` n `8`; equity avg `0.013` n `132`; fx avg `-0.0292` n `6`; index avg `0.0047` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.0485` n `790`
- 4h: commodity avg `-0.111` n `12`; crypto_alt avg `-1.2449` n `232`; crypto_major avg `-1.3853` n `8`; equity avg `-0.5907` n `132`; fx avg `-0.0404` n `6`; index avg `-0.0781` n `26`; metal avg `-0.0917` n `20`; unknown avg `-0.128` n `790`
- 24h: commodity avg `0.6248` n `12`; crypto_alt avg `-1.5697` n `232`; crypto_major avg `-2.6487` n `8`; equity avg `-2.0214` n `130`; fx avg `-0.2241` n `6`; index avg `-0.3444` n `26`; metal avg `-0.5783` n `20`; unknown avg `-0.5447` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
