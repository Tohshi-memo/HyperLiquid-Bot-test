# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T19:14:30.830603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1859` n `12`; crypto_alt avg `0.2827` n `230`; crypto_major avg `0.3363` n `8`; equity avg `0.3629` n `112`; fx avg `-0.0048` n `6`; index avg `0.0913` n `25`; metal avg `0.0756` n `20`; unknown avg `-0.0565` n `782`
- 1h: commodity avg `-0.2412` n `12`; crypto_alt avg `0.085` n `230`; crypto_major avg `0.0621` n `8`; equity avg `0.2218` n `112`; fx avg `0.0027` n `6`; index avg `0.0616` n `25`; metal avg `0.0678` n `20`; unknown avg `-0.0854` n `782`
- 4h: commodity avg `-0.2308` n `12`; crypto_alt avg `0.0996` n `230`; crypto_major avg `-0.4759` n `8`; equity avg `0.4821` n `112`; fx avg `-0.0222` n `6`; index avg `0.0689` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.1471` n `782`
- 24h: commodity avg `0.1771` n `12`; crypto_alt avg `-0.4053` n `230`; crypto_major avg `-0.5767` n `8`; equity avg `0.824` n `112`; fx avg `-0.1388` n `6`; index avg `0.021` n `25`; metal avg `0.3685` n `20`; unknown avg `-0.0982` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2395`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1855`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
