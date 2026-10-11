# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T17:07:32.418821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `13`; crypto_alt avg `-0.0337` n `235`; crypto_major avg `-0.2545` n `8`; equity avg `-0.0228` n `150`; fx avg `0.0102` n `6`; index avg `-0.0058` n `26`; metal avg `0.0148` n `20`; unknown avg `0.4738` n `1132`
- 1h: commodity avg `-0.0015` n `13`; crypto_alt avg `0.0884` n `235`; crypto_major avg `-0.0275` n `8`; equity avg `0.0735` n `150`; fx avg `0.0109` n `6`; index avg `0.0175` n `26`; metal avg `0.0513` n `20`; unknown avg `0.9928` n `1132`
- 4h: commodity avg `-0.0614` n `13`; crypto_alt avg `1.9782` n `235`; crypto_major avg `1.3934` n `8`; equity avg `0.2591` n `150`; fx avg `-0.0075` n `6`; index avg `0.0333` n `26`; metal avg `0.0657` n `20`; unknown avg `22.3565` n `1110`
- 24h: commodity avg `0.2823` n `13`; crypto_alt avg `2.3547` n `235`; crypto_major avg `1.0213` n `8`; equity avg `0.332` n `150`; fx avg `0.0204` n `6`; index avg `0.0369` n `26`; metal avg `0.0902` n `20`; unknown avg `1.4783` n `925`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
