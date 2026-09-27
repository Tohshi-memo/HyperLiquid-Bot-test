# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T08:07:26.124109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `-0.0118` n `234`; crypto_major avg `0.3209` n `8`; equity avg `0.051` n `141`; fx avg `-0.0004` n `6`; index avg `0.0056` n `26`; metal avg `-0.0003` n `20`; unknown avg `1.7726` n `943`
- 1h: commodity avg `-0.0345` n `12`; crypto_alt avg `0.6219` n `234`; crypto_major avg `0.8289` n `8`; equity avg `0.0922` n `141`; fx avg `-0.0048` n `6`; index avg `0.0108` n `26`; metal avg `0.0053` n `20`; unknown avg `1.755` n `943`
- 4h: commodity avg `-0.0146` n `12`; crypto_alt avg `1.6103` n `234`; crypto_major avg `1.1234` n `8`; equity avg `0.1474` n `141`; fx avg `0.0046` n `6`; index avg `0.0193` n `26`; metal avg `0.0053` n `20`; unknown avg `4.6855` n `923`
- 24h: commodity avg `-0.0066` n `12`; crypto_alt avg `1.5506` n `234`; crypto_major avg `0.9437` n `8`; equity avg `0.3695` n `141`; fx avg `-0.0028` n `6`; index avg `0.0239` n `26`; metal avg `0.0056` n `20`; unknown avg `3.3918` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
