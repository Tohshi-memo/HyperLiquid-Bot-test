# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T18:52:34.437441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.91` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0406` n `12`; crypto_alt avg `0.6977` n `230`; crypto_major avg `0.7215` n `8`; equity avg `1.2128` n `102`; fx avg `-0.0036` n `6`; index avg `0.1954` n `25`; metal avg `0.3336` n `20`; unknown avg `0.0768` n `778`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.6094` n `230`; crypto_major avg `0.674` n `8`; equity avg `1.5227` n `102`; fx avg `0.0158` n `6`; index avg `0.3435` n `25`; metal avg `0.5717` n `18`; unknown avg `-0.2296` n `763`
- 4h: commodity avg `-0.0304` n `12`; crypto_alt avg `1.0005` n `230`; crypto_major avg `1.0065` n `8`; equity avg `2.0812` n `102`; fx avg `-0.0051` n `6`; index avg `0.4988` n `25`; metal avg `0.8292` n `20`; unknown avg `-0.1329` n `778`
- 24h: commodity avg `1.3432` n `12`; crypto_alt avg `-0.9808` n `230`; crypto_major avg `1.0173` n `8`; equity avg `0.1744` n `102`; fx avg `-0.0538` n `6`; index avg `0.0158` n `25`; metal avg `0.5724` n `20`; unknown avg `-0.5752` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
