# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T11:07:28.409549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5608` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5126` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.067` n `12`; crypto_alt avg `0.0539` n `232`; crypto_major avg `0.1466` n `8`; equity avg `-0.1006` n `132`; fx avg `-0.0063` n `6`; index avg `-0.0044` n `26`; metal avg `0.0747` n `20`; unknown avg `0.0757` n `790`
- 1h: commodity avg `-0.0572` n `12`; crypto_alt avg `-0.3388` n `232`; crypto_major avg `-0.1505` n `8`; equity avg `-0.1363` n `132`; fx avg `-0.0292` n `6`; index avg `-0.0063` n `26`; metal avg `0.0674` n `20`; unknown avg `-0.1016` n `790`
- 4h: commodity avg `-0.006` n `12`; crypto_alt avg `-1.7625` n `232`; crypto_major avg `-1.6711` n `8`; equity avg `-0.9056` n `132`; fx avg `-0.0424` n `6`; index avg `-0.1585` n `26`; metal avg `-0.1103` n `20`; unknown avg `-0.0239` n `790`
- 24h: commodity avg `0.5358` n `12`; crypto_alt avg `-1.5471` n `232`; crypto_major avg `-2.4988` n `8`; equity avg `-1.9145` n `130`; fx avg `-0.2376` n `6`; index avg `-0.3077` n `26`; metal avg `-0.4426` n `20`; unknown avg `0.0236` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
