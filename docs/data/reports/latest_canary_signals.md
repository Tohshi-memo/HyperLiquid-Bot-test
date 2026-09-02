# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T05:22:24.669151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0439` n `12`; crypto_alt avg `0.3788` n `232`; crypto_major avg `0.3214` n `8`; equity avg `0.1733` n `132`; fx avg `-0.0103` n `6`; index avg `0.0369` n `26`; metal avg `0.0484` n `20`; unknown avg `0.4526` n `792`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `0.5207` n `232`; crypto_major avg `0.3513` n `8`; equity avg `0.1751` n `132`; fx avg `-0.0448` n `6`; index avg `0.0285` n `26`; metal avg `0.0876` n `20`; unknown avg `5.1032` n `790`
- 4h: commodity avg `-0.1947` n `12`; crypto_alt avg `1.0374` n `232`; crypto_major avg `0.4964` n `8`; equity avg `-0.1562` n `132`; fx avg `-0.0852` n `6`; index avg `-0.0578` n `26`; metal avg `-0.0433` n `20`; unknown avg `0.1196` n `790`
- 24h: commodity avg `0.7607` n `12`; crypto_alt avg `-0.3844` n `232`; crypto_major avg `-1.5346` n `8`; equity avg `-2.3025` n `130`; fx avg `-0.1176` n `6`; index avg `-0.4138` n `26`; metal avg `-0.9458` n `20`; unknown avg `-0.4013` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0429`, n `668`, weak_sample_signal
