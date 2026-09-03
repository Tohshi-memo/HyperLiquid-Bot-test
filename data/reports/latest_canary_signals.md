# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T11:41:39.688923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0607` n `12`; crypto_alt avg `0.2255` n `232`; crypto_major avg `0.2832` n `8`; equity avg `-0.089` n `133`; fx avg `0.0222` n `6`; index avg `0.004` n `26`; metal avg `0.0332` n `20`; unknown avg `1.5054` n `792`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `0.5532` n `232`; crypto_major avg `0.8209` n `8`; equity avg `0.2096` n `133`; fx avg `-0.0292` n `6`; index avg `0.0541` n `26`; metal avg `0.1015` n `20`; unknown avg `1.7638` n `790`
- 4h: commodity avg `0.4032` n `12`; crypto_alt avg `0.2094` n `232`; crypto_major avg `0.2815` n `8`; equity avg `-0.1877` n `133`; fx avg `-0.0965` n `6`; index avg `-0.0203` n `26`; metal avg `0.0171` n `20`; unknown avg `0.4437` n `790`
- 24h: commodity avg `0.7433` n `12`; crypto_alt avg `2.2348` n `232`; crypto_major avg `2.2342` n `8`; equity avg `1.423` n `133`; fx avg `-0.3697` n `6`; index avg `0.0819` n `26`; metal avg `0.6282` n `20`; unknown avg `-0.1219` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0419`, n `668`, weak_sample_signal
