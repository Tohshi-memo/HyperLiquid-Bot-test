# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T14:52:30.223506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `0.0172` n `230`; crypto_major avg `-0.0333` n `8`; equity avg `-0.2971` n `109`; fx avg `-0.0207` n `6`; index avg `-0.0634` n `25`; metal avg `-0.0323` n `20`; unknown avg `0.0388` n `781`
- 1h: commodity avg `0.057` n `12`; crypto_alt avg `0.0581` n `230`; crypto_major avg `0.2323` n `8`; equity avg `0.8555` n `109`; fx avg `0.0213` n `6`; index avg `0.066` n `25`; metal avg `0.1135` n `20`; unknown avg `0.2164` n `781`
- 4h: commodity avg `-0.0145` n `12`; crypto_alt avg `0.4966` n `230`; crypto_major avg `0.1088` n `8`; equity avg `1.3226` n `109`; fx avg `0.0297` n `6`; index avg `0.1249` n `25`; metal avg `-0.1409` n `20`; unknown avg `0.4086` n `781`
- 24h: commodity avg `0.2329` n `12`; crypto_alt avg `0.4664` n `230`; crypto_major avg `-0.6113` n `8`; equity avg `-0.0801` n `109`; fx avg `0.0264` n `6`; index avg `-0.2297` n `25`; metal avg `0.1602` n `20`; unknown avg `113.3661` n `749`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
