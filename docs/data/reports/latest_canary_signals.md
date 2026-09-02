# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T00:22:25.844834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0624` n `12`; crypto_alt avg `0.0839` n `232`; crypto_major avg `0.066` n `8`; equity avg `0.2356` n `132`; fx avg `-0.0139` n `6`; index avg `0.0391` n `26`; metal avg `0.0441` n `20`; unknown avg `2.4971` n `792`
- 1h: commodity avg `0.0354` n `12`; crypto_alt avg `0.4817` n `232`; crypto_major avg `0.3253` n `8`; equity avg `0.3046` n `132`; fx avg `-0.0587` n `6`; index avg `0.0599` n `26`; metal avg `0.0249` n `20`; unknown avg `0.0728` n `790`
- 4h: commodity avg `0.0644` n `12`; crypto_alt avg `0.0719` n `232`; crypto_major avg `0.1567` n `8`; equity avg `-0.0274` n `132`; fx avg `-0.0459` n `6`; index avg `0.0522` n `26`; metal avg `0.0183` n `20`; unknown avg `0.4647` n `772`
- 24h: commodity avg `0.8538` n `12`; crypto_alt avg `-0.7867` n `232`; crypto_major avg `-1.7577` n `8`; equity avg `-1.8824` n `130`; fx avg `0.0187` n `6`; index avg `-0.2937` n `26`; metal avg `-0.9821` n `20`; unknown avg `0.1466` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0437`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0436`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0407`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0325`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0302`, n `668`, weak_sample_signal
