# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T14:07:40.892114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0667` n `13`; crypto_alt avg `-0.1061` n `235`; crypto_major avg `-0.181` n `8`; equity avg `-0.0288` n `150`; fx avg `-0.0195` n `6`; index avg `0.0098` n `26`; metal avg `0.0434` n `20`; unknown avg `-0.1043` n `1062`
- 1h: commodity avg `-0.0078` n `13`; crypto_alt avg `-0.1967` n `235`; crypto_major avg `-0.2019` n `8`; equity avg `-0.2211` n `150`; fx avg `-0.0132` n `6`; index avg `-0.086` n `26`; metal avg `-0.0191` n `20`; unknown avg `0.3296` n `1028`
- 4h: commodity avg `0.0935` n `13`; crypto_alt avg `-0.7344` n `235`; crypto_major avg `-0.525` n `8`; equity avg `-0.6849` n `150`; fx avg `-0.0422` n `6`; index avg `-0.2052` n `26`; metal avg `-0.2475` n `20`; unknown avg `2.0929` n `1022`
- 24h: commodity avg `1.1399` n `13`; crypto_alt avg `-5.3332` n `235`; crypto_major avg `-3.8644` n `8`; equity avg `-2.2684` n `150`; fx avg `-0.18` n `6`; index avg `-0.5037` n `26`; metal avg `-0.6161` n `20`; unknown avg `826.5765` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
