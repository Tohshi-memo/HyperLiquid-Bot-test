# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T13:22:30.946457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.08` - Polymarket crypto volume is unusually high.
- 1h_commodity_crypto_divergence: score `-2.0032` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.9121` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.8989` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6852` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-1.6498` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0342` n `12`; crypto_alt avg `0.3068` n `232`; crypto_major avg `0.2167` n `8`; equity avg `0.165` n `133`; fx avg `-0.0203` n `6`; index avg `0.0206` n `26`; metal avg `0.0587` n `20`; unknown avg `1.3633` n `765`
- 1h: commodity avg `-0.0063` n `12`; crypto_alt avg `-1.81` n `232`; crypto_major avg `-2.0095` n `8`; equity avg `-0.7164` n `133`; fx avg `-0.0966` n `6`; index avg `-0.0974` n `26`; metal avg `-0.3597` n `20`; unknown avg `0.7085` n `743`
- 4h: commodity avg `-0.0109` n `12`; crypto_alt avg `-1.803` n `232`; crypto_major avg `-1.9759` n `8`; equity avg `-0.5644` n `133`; fx avg `-0.1587` n `6`; index avg `-0.077` n `26`; metal avg `-0.2907` n `20`; unknown avg `-0.0441` n `743`
- 24h: commodity avg `-0.3469` n `12`; crypto_alt avg `0.4638` n `232`; crypto_major avg `1.1845` n `8`; equity avg `1.0518` n `133`; fx avg `-0.1079` n `6`; index avg `0.2011` n `26`; metal avg `-0.1668` n `20`; unknown avg `1.1874` n `704`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
