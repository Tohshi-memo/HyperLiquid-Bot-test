# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T03:37:43.019264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `0.5958` n `228`; crypto_major avg `0.5161` n `8`; equity avg `0.2112` n `77`; fx avg `0.0104` n `6`; index avg `0.0449` n `23`; metal avg `0.2179` n `18`; unknown avg `4.0802` n `687`
- 1h: commodity avg `-0.1541` n `12`; crypto_alt avg `0.8366` n `228`; crypto_major avg `0.6263` n `8`; equity avg `0.292` n `77`; fx avg `0.0112` n `6`; index avg `0.0964` n `23`; metal avg `0.3086` n `18`; unknown avg `-0.396` n `679`
- 4h: commodity avg `-0.4316` n `12`; crypto_alt avg `0.2198` n `228`; crypto_major avg `0.2329` n `8`; equity avg `-0.0204` n `77`; fx avg `-0.0283` n `6`; index avg `0.1083` n `23`; metal avg `-0.1276` n `18`; unknown avg `-0.2522` n `671`
- 24h: commodity avg `0.3619` n `12`; crypto_alt avg `0.3778` n `228`; crypto_major avg `1.8393` n `8`; equity avg `1.0786` n `76`; fx avg `-0.0669` n `6`; index avg `0.5226` n `23`; metal avg `-0.2625` n `18`; unknown avg `0.917` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
