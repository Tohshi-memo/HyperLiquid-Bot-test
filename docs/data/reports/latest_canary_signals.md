# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T08:52:39.584091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0189` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0382` n `12`; crypto_alt avg `-0.4919` n `232`; crypto_major avg `-0.4962` n `8`; equity avg `-0.2182` n `132`; fx avg `0.0106` n `6`; index avg `-0.0481` n `26`; metal avg `-0.0572` n `20`; unknown avg `0.5306` n `792`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.6443` n `232`; crypto_major avg `-0.9472` n `8`; equity avg `-0.388` n `132`; fx avg `-0.0024` n `6`; index avg `-0.0446` n `26`; metal avg `-0.0582` n `20`; unknown avg `0.3039` n `790`
- 4h: commodity avg `-0.0585` n `12`; crypto_alt avg `-0.669` n `232`; crypto_major avg `-1.0591` n `8`; equity avg `-0.3092` n `132`; fx avg `-0.0779` n `6`; index avg `-0.0402` n `26`; metal avg `0.0794` n `20`; unknown avg `0.4847` n `770`
- 24h: commodity avg `0.5285` n `12`; crypto_alt avg `-0.2222` n `232`; crypto_major avg `-1.7083` n `8`; equity avg `-1.7837` n `130`; fx avg `-0.1866` n `6`; index avg `-0.2975` n `26`; metal avg `-0.4325` n `20`; unknown avg `-0.0065` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
