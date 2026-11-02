# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T05:37:27.220865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `0.0367` n `238`; crypto_major avg `0.1061` n `8`; equity avg `0.1537` n `156`; fx avg `-0.0022` n `6`; index avg `-0.014` n `27`; metal avg `0.0898` n `20`; unknown avg `129.4181` n `1259`
- 1h: commodity avg `-0.0669` n `13`; crypto_alt avg `-0.2193` n `238`; crypto_major avg `-0.2265` n `8`; equity avg `-0.1107` n `156`; fx avg `-0.0325` n `6`; index avg `0.0173` n `27`; metal avg `0.1558` n `20`; unknown avg `-0.5793` n `1251`
- 4h: commodity avg `-0.2955` n `13`; crypto_alt avg `-0.3712` n `238`; crypto_major avg `-0.2381` n `8`; equity avg `0.4849` n `156`; fx avg `0.074` n `6`; index avg `0.1301` n `27`; metal avg `0.0986` n `20`; unknown avg `2.1326` n `1191`
- 24h: commodity avg `-0.4918` n `13`; crypto_alt avg `-0.8484` n `238`; crypto_major avg `0.2982` n `8`; equity avg `1.3646` n `156`; fx avg `0.1887` n `6`; index avg `0.3876` n `27`; metal avg `0.214` n `20`; unknown avg `3.5077` n `1070`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
