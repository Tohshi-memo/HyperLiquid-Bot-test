# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T21:52:28.596270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0602` n `13`; crypto_alt avg `-0.4966` n `239`; crypto_major avg `-0.4449` n `8`; equity avg `-0.6985` n `163`; fx avg `-0.0066` n `6`; index avg `-0.0589` n `27`; metal avg `-0.0603` n `20`; unknown avg `0.3161` n `1265`
- 1h: commodity avg `0.0577` n `13`; crypto_alt avg `0.3414` n `239`; crypto_major avg `0.442` n `8`; equity avg `1.2262` n `163`; fx avg `-0.0195` n `6`; index avg `0.1423` n `27`; metal avg `0.087` n `20`; unknown avg `0.4845` n `1247`
- 4h: commodity avg `-0.0377` n `13`; crypto_alt avg `0.7229` n `239`; crypto_major avg `0.6685` n `8`; equity avg `1.189` n `163`; fx avg `-0.0345` n `6`; index avg `0.1145` n `27`; metal avg `-0.0726` n `20`; unknown avg `0.9539` n `1239`
- 24h: commodity avg `0.3374` n `13`; crypto_alt avg `-0.3175` n `239`; crypto_major avg `-0.4753` n `8`; equity avg `-0.5692` n `163`; fx avg `0.0178` n `6`; index avg `-0.0583` n `27`; metal avg `-0.0297` n `20`; unknown avg `9.9622` n `1107`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
