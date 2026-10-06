# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T22:07:33.895491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `13`; crypto_alt avg `0.2217` n `235`; crypto_major avg `0.1548` n `8`; equity avg `0.0075` n `150`; fx avg `-0.0058` n `6`; index avg `0.0027` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.0373` n `1066`
- 1h: commodity avg `-0.0016` n `13`; crypto_alt avg `0.0728` n `235`; crypto_major avg `0.0058` n `8`; equity avg `0.0111` n `150`; fx avg `-0.0035` n `6`; index avg `0.0053` n `26`; metal avg `0.0098` n `20`; unknown avg `-0.1219` n `1058`
- 4h: commodity avg `0.341` n `13`; crypto_alt avg `-0.4165` n `235`; crypto_major avg `-0.312` n `8`; equity avg `-0.3064` n `150`; fx avg `-0.0164` n `6`; index avg `-0.0438` n `26`; metal avg `-0.0067` n `20`; unknown avg `0.3226` n `990`
- 24h: commodity avg `0.3033` n `13`; crypto_alt avg `-1.5451` n `235`; crypto_major avg `-1.0975` n `8`; equity avg `0.3965` n `149`; fx avg `0.0896` n `6`; index avg `-0.005` n `26`; metal avg `0.0278` n `20`; unknown avg `871.0638` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
