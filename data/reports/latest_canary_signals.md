# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T11:52:26.713207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2085` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.0863` n `232`; crypto_major avg `-0.0263` n `8`; equity avg `-0.0877` n `132`; fx avg `0.0137` n `6`; index avg `-0.0171` n `26`; metal avg `0.0023` n `20`; unknown avg `0.0628` n `792`
- 1h: commodity avg `-0.2707` n `12`; crypto_alt avg `0.3272` n `232`; crypto_major avg `0.3811` n `8`; equity avg `0.2785` n `132`; fx avg `-0.033` n `6`; index avg `0.0931` n `26`; metal avg `0.2838` n `20`; unknown avg `0.2274` n `790`
- 4h: commodity avg `-0.2249` n `12`; crypto_alt avg `-1.3028` n `232`; crypto_major avg `-1.2313` n `8`; equity avg `-0.4666` n `132`; fx avg `-0.0572` n `6`; index avg `-0.0228` n `26`; metal avg `0.1382` n `20`; unknown avg `-0.2874` n `790`
- 24h: commodity avg `0.4291` n `12`; crypto_alt avg `-1.8255` n `232`; crypto_major avg `-2.6564` n `8`; equity avg `-1.6058` n `130`; fx avg `-0.2625` n `6`; index avg `-0.2267` n `26`; metal avg `-0.2943` n `20`; unknown avg `-0.3745` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
