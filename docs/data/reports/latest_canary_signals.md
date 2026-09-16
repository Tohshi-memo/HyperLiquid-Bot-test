# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T01:52:30.612215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0274` n `12`; crypto_alt avg `-0.3404` n `234`; crypto_major avg `-0.1563` n `8`; equity avg `-0.068` n `137`; fx avg `0.0039` n `6`; index avg `-0.0167` n `27`; metal avg `-0.0252` n `20`; unknown avg `-0.2263` n `919`
- 1h: commodity avg `0.0416` n `12`; crypto_alt avg `-0.8092` n `234`; crypto_major avg `-0.4872` n `8`; equity avg `-0.2105` n `137`; fx avg `0.0167` n `6`; index avg `-0.0411` n `27`; metal avg `-0.0264` n `20`; unknown avg `0.0654` n `917`
- 4h: commodity avg `-0.012` n `12`; crypto_alt avg `-0.6269` n `234`; crypto_major avg `-0.1573` n `8`; equity avg `-0.0991` n `137`; fx avg `0.1422` n `6`; index avg `-0.0105` n `27`; metal avg `-0.0453` n `20`; unknown avg `-0.2074` n `879`
- 24h: commodity avg `0.3687` n `12`; crypto_alt avg `-4.5977` n `234`; crypto_major avg `-4.4082` n `8`; equity avg `-1.5457` n `137`; fx avg `0.3017` n `6`; index avg `-0.1568` n `27`; metal avg `0.1725` n `20`; unknown avg `0.8513` n `802`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
