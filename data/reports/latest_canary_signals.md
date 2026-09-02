# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T11:22:36.250126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7363` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6388` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.104` n `12`; crypto_alt avg `-0.034` n `232`; crypto_major avg `-0.1206` n `8`; equity avg `0.2507` n `132`; fx avg `-0.0163` n `6`; index avg `0.0666` n `26`; metal avg `0.1087` n `20`; unknown avg `0.2016` n `792`
- 1h: commodity avg `-0.0915` n `12`; crypto_alt avg `-0.3999` n `232`; crypto_major avg `-0.3772` n `8`; equity avg `0.0249` n `132`; fx avg `-0.0348` n `6`; index avg `0.0392` n `26`; metal avg `0.1195` n `20`; unknown avg `0.4334` n `790`
- 4h: commodity avg `-0.1295` n `12`; crypto_alt avg `-1.6793` n `232`; crypto_major avg `-1.727` n `8`; equity avg `-0.7017` n `132`; fx avg `-0.0563` n `6`; index avg `-0.0882` n `26`; metal avg `0.0093` n `20`; unknown avg `0.2131` n `790`
- 24h: commodity avg `0.4955` n `12`; crypto_alt avg `-1.6751` n `232`; crypto_major avg `-2.6806` n `8`; equity avg `-1.6563` n `130`; fx avg `-0.2573` n `6`; index avg `-0.2449` n `26`; metal avg `-0.3039` n `20`; unknown avg `0.0566` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0441`, n `668`, weak_sample_signal
