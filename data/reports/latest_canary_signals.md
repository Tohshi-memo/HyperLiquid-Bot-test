# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T15:07:26.843280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0248` n `230`; crypto_major avg `-0.0014` n `8`; equity avg `0.0067` n `102`; fx avg `-0.0053` n `6`; index avg `0.0056` n `25`; metal avg `-0.0027` n `20`; unknown avg `2.4248` n `782`
- 1h: commodity avg `0.0188` n `12`; crypto_alt avg `0.1332` n `230`; crypto_major avg `0.1573` n `8`; equity avg `0.0264` n `102`; fx avg `-0.0212` n `6`; index avg `0.02` n `25`; metal avg `0.0039` n `20`; unknown avg `2.3078` n `782`
- 4h: commodity avg `-0.0409` n `12`; crypto_alt avg `0.0001` n `230`; crypto_major avg `-0.0276` n `8`; equity avg `-0.1663` n `102`; fx avg `-0.0114` n `6`; index avg `-0.0227` n `25`; metal avg `0.0098` n `20`; unknown avg `1.0755` n `782`
- 24h: commodity avg `-1.0722` n `12`; crypto_alt avg `0.194` n `230`; crypto_major avg `0.045` n `8`; equity avg `0.8553` n `102`; fx avg `-0.1517` n `6`; index avg `0.2385` n `25`; metal avg `0.251` n `20`; unknown avg `1.4348` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
