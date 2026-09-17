# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T14:22:35.271094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `0.8256` n `234`; crypto_major avg `0.7375` n `8`; equity avg `0.2589` n `138`; fx avg `-0.0142` n `6`; index avg `0.0426` n `26`; metal avg `-0.0059` n `20`; unknown avg `1.8637` n `919`
- 1h: commodity avg `0.2219` n `12`; crypto_alt avg `0.6057` n `234`; crypto_major avg `0.3669` n `8`; equity avg `-0.1172` n `138`; fx avg `0.0039` n `6`; index avg `-0.0183` n `26`; metal avg `0.0296` n `20`; unknown avg `0.8766` n `899`
- 4h: commodity avg `0.0728` n `12`; crypto_alt avg `1.2191` n `234`; crypto_major avg `1.3622` n `8`; equity avg `0.4571` n `138`; fx avg `-0.0882` n `6`; index avg `0.1518` n `26`; metal avg `0.4251` n `20`; unknown avg `1.7274` n `893`
- 24h: commodity avg `-0.4374` n `12`; crypto_alt avg `5.0111` n `234`; crypto_major avg `3.1096` n `8`; equity avg `1.6187` n `138`; fx avg `0.0276` n `6`; index avg `0.2526` n `26`; metal avg `0.3469` n `20`; unknown avg `0.4422` n `713`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
