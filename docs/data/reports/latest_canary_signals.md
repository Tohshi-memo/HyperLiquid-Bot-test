# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T10:52:26.364574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5892` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.576` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `-0.2546` n `232`; crypto_major avg `-0.2477` n `8`; equity avg `-0.0672` n `132`; fx avg `0.0004` n `6`; index avg `-0.0101` n `26`; metal avg `-0.0252` n `20`; unknown avg `0.4307` n `792`
- 1h: commodity avg `0.0406` n `12`; crypto_alt avg `-0.7813` n `232`; crypto_major avg `-0.5582` n `8`; equity avg `-0.088` n `132`; fx avg `-0.0185` n `6`; index avg `-0.0062` n `26`; metal avg `-0.0264` n `20`; unknown avg `0.3381` n `790`
- 4h: commodity avg `-0.0817` n `12`; crypto_alt avg `-1.6671` n `232`; crypto_major avg `-1.7005` n `8`; equity avg `-0.6804` n `132`; fx avg `-0.0147` n `6`; index avg `-0.1113` n `26`; metal avg `-0.1245` n `20`; unknown avg `0.1614` n `790`
- 24h: commodity avg `0.6114` n `12`; crypto_alt avg `-1.7169` n `232`; crypto_major avg `-2.7557` n `8`; equity avg `-1.9263` n `130`; fx avg `-0.2291` n `6`; index avg `-0.3146` n `26`; metal avg `-0.5248` n `20`; unknown avg `-0.0808` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
