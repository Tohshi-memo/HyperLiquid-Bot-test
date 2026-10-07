# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T21:37:35.184982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `-0.3018` n `235`; crypto_major avg `-0.3018` n `8`; equity avg `-0.0069` n `150`; fx avg `-0.0043` n `6`; index avg `-0.0119` n `26`; metal avg `0.0048` n `20`; unknown avg `-0.1785` n `1077`
- 1h: commodity avg `-0.0589` n `13`; crypto_alt avg `-0.1818` n `235`; crypto_major avg `-0.259` n `8`; equity avg `0.0487` n `150`; fx avg `0.0033` n `6`; index avg `0.008` n `26`; metal avg `0.0178` n `20`; unknown avg `-0.2487` n `1067`
- 4h: commodity avg `0.3238` n `13`; crypto_alt avg `0.3583` n `235`; crypto_major avg `-0.1616` n `8`; equity avg `0.0325` n `150`; fx avg `0.0308` n `6`; index avg `0.0004` n `26`; metal avg `-0.0681` n `20`; unknown avg `0.3992` n `999`
- 24h: commodity avg `0.3836` n `13`; crypto_alt avg `-4.4591` n `235`; crypto_major avg `-3.7128` n `8`; equity avg `-1.4034` n `150`; fx avg `-0.1548` n `6`; index avg `-0.2345` n `26`; metal avg `-0.6872` n `20`; unknown avg `1.1875` n `972`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
