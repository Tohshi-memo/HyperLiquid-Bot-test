# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T13:07:28.605161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0377` n `12`; crypto_alt avg `-0.0653` n `232`; crypto_major avg `0.1008` n `8`; equity avg `0.1193` n `134`; fx avg `-0.001` n `6`; index avg `0.0157` n `26`; metal avg `0.097` n `20`; unknown avg `0.6792` n `795`
- 1h: commodity avg `-0.2896` n `12`; crypto_alt avg `0.3001` n `232`; crypto_major avg `0.3676` n `8`; equity avg `0.2966` n `134`; fx avg `-0.0366` n `6`; index avg `0.0858` n `26`; metal avg `0.085` n `20`; unknown avg `0.5864` n `789`
- 4h: commodity avg `-0.2823` n `12`; crypto_alt avg `0.032` n `232`; crypto_major avg `0.0186` n `8`; equity avg `0.769` n `134`; fx avg `-0.0244` n `6`; index avg `0.1448` n `26`; metal avg `0.158` n `20`; unknown avg `0.4938` n `789`
- 24h: commodity avg `-0.0733` n `12`; crypto_alt avg `-0.8947` n `232`; crypto_major avg `-1.5159` n `8`; equity avg `0.2354` n `134`; fx avg `-0.1354` n `6`; index avg `0.028` n `26`; metal avg `0.2336` n `20`; unknown avg `0.3107` n `710`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
