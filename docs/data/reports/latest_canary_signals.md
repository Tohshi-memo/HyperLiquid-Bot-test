# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T23:52:27.032549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `13`; crypto_alt avg `0.1437` n `236`; crypto_major avg `0.0314` n `8`; equity avg `0.0955` n `151`; fx avg `-0.0007` n `6`; index avg `0.0048` n `26`; metal avg `0.011` n `20`; unknown avg `0.0161` n `1193`
- 1h: commodity avg `0.0689` n `13`; crypto_alt avg `0.1618` n `236`; crypto_major avg `0.007` n `8`; equity avg `0.029` n `151`; fx avg `0.0075` n `6`; index avg `-0.0235` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.0434` n `1191`
- 4h: commodity avg `0.0728` n `13`; crypto_alt avg `0.7838` n `236`; crypto_major avg `0.6008` n `8`; equity avg `-0.1648` n `151`; fx avg `0.0069` n `6`; index avg `-0.0418` n `26`; metal avg `0.0055` n `20`; unknown avg `0.6315` n `1107`
- 24h: commodity avg `0.4842` n `13`; crypto_alt avg `-0.9401` n `236`; crypto_major avg `-0.9331` n `8`; equity avg `-3.6394` n `151`; fx avg `0.0382` n `6`; index avg `-0.5914` n `26`; metal avg `-0.0135` n `20`; unknown avg `40.6124` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1679`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.118`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0883`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0771`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0716`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0696`, n `666`, weak_sample_signal
