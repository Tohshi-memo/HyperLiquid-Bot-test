# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T23:37:28.970130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `13`; crypto_alt avg `0.1172` n `235`; crypto_major avg `0.0456` n `8`; equity avg `-0.0105` n `150`; fx avg `0.0168` n `6`; index avg `-0.0027` n `26`; metal avg `0.0029` n `20`; unknown avg `0.0721` n `1117`
- 1h: commodity avg `-0.005` n `13`; crypto_alt avg `-0.1873` n `235`; crypto_major avg `-0.0595` n `8`; equity avg `-0.0172` n `150`; fx avg `0.0108` n `6`; index avg `-0.004` n `26`; metal avg `-0.0002` n `20`; unknown avg `3.0707` n `1115`
- 4h: commodity avg `0.1665` n `13`; crypto_alt avg `-0.0275` n `235`; crypto_major avg `-0.1853` n `8`; equity avg `0.0146` n `150`; fx avg `0.0117` n `6`; index avg `0.0063` n `26`; metal avg `0.0132` n `20`; unknown avg `4.4266` n `1071`
- 24h: commodity avg `0.0542` n `13`; crypto_alt avg `1.9276` n `235`; crypto_major avg `0.7433` n `8`; equity avg `0.1861` n `150`; fx avg `0.0068` n `6`; index avg `0.0161` n `26`; metal avg `0.0154` n `20`; unknown avg `0.355` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
