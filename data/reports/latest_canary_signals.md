# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T12:37:30.383245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0266` n `12`; crypto_alt avg `-0.1009` n `234`; crypto_major avg `0.0572` n `8`; equity avg `0.1736` n `137`; fx avg `0.0244` n `6`; index avg `0.04` n `27`; metal avg `-0.0526` n `20`; unknown avg `-0.2837` n `915`
- 1h: commodity avg `-0.1915` n `12`; crypto_alt avg `0.607` n `234`; crypto_major avg `1.0842` n `8`; equity avg `0.5288` n `137`; fx avg `-0.0327` n `6`; index avg `0.1557` n `27`; metal avg `0.2783` n `20`; unknown avg `0.026` n `913`
- 4h: commodity avg `-0.3325` n `12`; crypto_alt avg `0.2732` n `234`; crypto_major avg `0.5153` n `8`; equity avg `0.694` n `137`; fx avg `-0.0758` n `6`; index avg `0.2339` n `27`; metal avg `0.2838` n `20`; unknown avg `0.5547` n `913`
- 24h: commodity avg `-0.8533` n `12`; crypto_alt avg `3.5036` n `234`; crypto_major avg `2.1466` n `8`; equity avg `1.8516` n `137`; fx avg `0.0498` n `6`; index avg `0.2669` n `27`; metal avg `0.2202` n `20`; unknown avg `0.5265` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
