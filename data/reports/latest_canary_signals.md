# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T10:07:25.018603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4723` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0308` n `12`; crypto_alt avg `-0.3909` n `232`; crypto_major avg `-0.2626` n `8`; equity avg `-0.0523` n `132`; fx avg `0.0044` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0191` n `20`; unknown avg `0.4564` n `790`
- 1h: commodity avg `0.0489` n `12`; crypto_alt avg `-0.8724` n `232`; crypto_major avg `-0.7189` n `8`; equity avg `-0.3265` n `132`; fx avg `-0.0044` n `6`; index avg `-0.0616` n `26`; metal avg `-0.1044` n `20`; unknown avg `-0.1589` n `790`
- 4h: commodity avg `-0.0877` n `12`; crypto_alt avg `-1.3645` n `232`; crypto_major avg `-1.5773` n `8`; equity avg `-0.7568` n `132`; fx avg `-0.0003` n `6`; index avg `-0.105` n `26`; metal avg `-0.1527` n `20`; unknown avg `1.1156` n `786`
- 24h: commodity avg `0.6034` n `12`; crypto_alt avg `-0.7451` n `232`; crypto_major avg `-2.0725` n `8`; equity avg `-1.8955` n `130`; fx avg `-0.2038` n `6`; index avg `-0.3108` n `26`; metal avg `-0.4709` n `20`; unknown avg `0.0499` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
