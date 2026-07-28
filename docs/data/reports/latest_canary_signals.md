# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T06:22:30.690505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0559` n `12`; crypto_alt avg `0.226` n `230`; crypto_major avg `0.2124` n `8`; equity avg `0.0233` n `102`; fx avg `0.0173` n `6`; index avg `0.027` n `25`; metal avg `0.0383` n `20`; unknown avg `0.0523` n `774`
- 1h: commodity avg `0.0928` n `12`; crypto_alt avg `-0.0526` n `230`; crypto_major avg `-0.3295` n `8`; equity avg `-0.285` n `102`; fx avg `-0.0128` n `6`; index avg `-0.0216` n `25`; metal avg `0.0267` n `20`; unknown avg `-0.0317` n `758`
- 4h: commodity avg `0.0876` n `12`; crypto_alt avg `0.0691` n `230`; crypto_major avg `-0.2519` n `8`; equity avg `-0.7289` n `102`; fx avg `-0.0567` n `6`; index avg `-0.138` n `25`; metal avg `-0.0456` n `20`; unknown avg `-0.069` n `758`
- 24h: commodity avg `-0.4886` n `12`; crypto_alt avg `-3.8809` n `230`; crypto_major avg `-3.8189` n `8`; equity avg `-4.1727` n `102`; fx avg `-0.1731` n `6`; index avg `-0.8871` n `25`; metal avg `-0.3821` n `20`; unknown avg `1129.1368` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
