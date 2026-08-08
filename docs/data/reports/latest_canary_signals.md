# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T05:07:33.352312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `0.0164` n `230`; crypto_major avg `-0.0173` n `8`; equity avg `-0.0347` n `112`; fx avg `0.0008` n `6`; index avg `-0.0046` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.0019` n `783`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `-0.0123` n `230`; crypto_major avg `-0.0392` n `8`; equity avg `-0.1011` n `112`; fx avg `0.0008` n `6`; index avg `-0.0384` n `25`; metal avg `-0.0244` n `20`; unknown avg `0.3248` n `783`
- 4h: commodity avg `-0.0003` n `12`; crypto_alt avg `0.4155` n `230`; crypto_major avg `0.456` n `8`; equity avg `-0.0839` n `112`; fx avg `-0.0027` n `6`; index avg `-0.0068` n `25`; metal avg `-0.059` n `20`; unknown avg `0.0371` n `783`
- 24h: commodity avg `-0.2416` n `12`; crypto_alt avg `0.1976` n `230`; crypto_major avg `0.904` n `8`; equity avg `1.5529` n `112`; fx avg `-0.0657` n `6`; index avg `0.1546` n `25`; metal avg `0.3451` n `20`; unknown avg `0.0217` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
